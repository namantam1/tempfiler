from django.core.files.storage import default_storage
from datetime import datetime
import uuid
import os

class ImageUploader:

    def get_file_path(self, file, typ):
        now = datetime.now()
        _, ext = os.path.splitext(file.name)
        data = {
            'type': typ,
            'year': str(now.year)[:2],
            'month': now.strftime('%b'),
            'hash': uuid.uuid4().hex[:8] + ext,
        }
        return '{type}/{year}/{month}/{hash}'.format(**data)

    def upload(self, image, typ):
        img_res = default_storage.save(self.get_file_path(image, typ), image)
        return default_storage.url(img_res)

image_uploader = ImageUploader()