from rest_framework.test import APIRequestFactory

from django.test import TestCase
from django.utils.timezone import now, localtime
from django.core.management import call_command

from datetime import timedelta
from time import sleep
import os
import io

from .views import UploadFile, GetFileDelete, DeleteExpired


upload_view = UploadFile.as_view()
get_view = GetFileDelete.as_view()
delete_expired_view = DeleteExpired.as_view()


def get_now():
    """return local now time"""
    return localtime(now())


# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()


def upload_request(time=5):
    """
    return request of upload
    """
    temp = io.BytesIO(b"hello")
    temp.name = "test.png"

    req = factory.post("/upload/", {
        "expire_on": get_now() + timedelta(seconds=time),
        "myfile": temp
    })

    return req

# Create your tests here.


class FileTestCase(TestCase):
    # def setUp(self):
    #     print("setup")

    def check_path(self, url):
        return os.path.exists("/".join(url.split("/")[3:]))

    def test_upload_api(self):
        """
        check for upload api
        """
        print("\n-> test upload api**")

        req = upload_request()
        res = upload_view(req)

        self.assertEqual(res.status_code, 201)
        self.assertIn("id", res.data)
        self.assertIn("timestamp", res.data)
        self.assertIn("expire_on", res.data)
        self.assertIn("myfile", res.data)
        self.assertTrue(self.check_path(res.data['myfile']))

        print("slept deleting... ")
        sleep(5)
        call_command("delete_file")
        self.assertFalse(self.check_path(res.data['myfile']))

    def test_valid_time(self):
        """
        validate expire on fields
        """
        
        print("\n-> test valid time**")


        day_31 = 31 * 24 * 60 * 60

        req = upload_request(day_31)
        res = upload_view(req)

        self.assertEqual(res.status_code, 400)
        print(res.data)

        yesterday = -60
        req = upload_request(yesterday)
        res = upload_view(req)

        self.assertEqual(res.status_code, 400)
        print(res.data)

    def test_delete_expired(self):
        """
        check for delete api
        """
        print("\n-> test delete expired**")

        req = upload_request()
        res = upload_view(req)

        self.assertIn("myfile", res.data)
        self.assertTrue(self.check_path(res.data['myfile']))

        print("slept deleting... ")
        sleep(5)

        res1 = delete_expired_view(factory.get("/delete/"))

        self.assertEqual(res1.status_code, 200)
        self.assertFalse(self.check_path(res.data['myfile']))

