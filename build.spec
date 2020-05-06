version: 0.1
phases:
  install:
    commands:
      - aws cloudformation package --template-file template.yaml --s3-bucket quotesappdemosls --output-template-file outputSamTemplate.yaml
artifacts:
  type: zip
  files:
    - template.yaml
    - outputSamTemplate.yaml
