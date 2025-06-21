import boto3
import os

def download_csv_from_s3():
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )
    local_path=os.path.join(os.path.dirname(__file__), 'static', 'movie_dataset.csv')
    s3.download_file('movieaisite', 'movie_dataset.csv', local_path)
    return
 
    
