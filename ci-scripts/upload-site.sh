#!/bin/bash

echo "s3cmd --access_key=${AWS_ACCESS_KEY_ID} --secret_key=${AWS_SECRET_ACCESS_KEY} --region=ap-southeast-1 sync --delete-removed --acl-public --guess-mime-type --no-mime-magic --recursive public/ s3://www.skycoin.net/docs/"
s3cmd --access_key="${AWS_ACCESS_KEY_ID}" --secret_key="${AWS_SECRET_ACCESS_KEY}" --region=ap-southeast-1 sync --delete-removed --acl-public --guess-mime-type --no-mime-magic --recursive public/ s3://www.skycoin.net/docs/
