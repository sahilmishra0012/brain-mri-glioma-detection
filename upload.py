from google.cloud import storage


def make_blob_public():
    """Makes a blob publicly accessible."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"

    storage_client = storage.Client.from_service_account_json('gcs.json')
    bucket = storage_client.bucket('pathology-bucket')
    blob = bucket.blob('image.png')

    blob.upload_from_filename('image.png')

    print(
        "File {} uploaded to {}.".format(
            'image.png', 'image.png'
        )
    )

make_blob_public()