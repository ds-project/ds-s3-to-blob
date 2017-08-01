# ds-s3-to-blob
Transfer AWS s3 to Azure blob storage

We should use ```python 3.5.2``` on Azure Function.

(Follow [this instruction link](https://prmadi.com/running-python-code-on-azure-functions-app/) to install python 3.5.2 )

Then, install azure sdk on python 3.5.2

```
> cd /d/home/site/tools/
> python -m pip install azure 
```

Then, put some configs on file and send post request and put body just following as json type.   

```json
{
    "url": "https://s3.ap-northeast-2.amazonaws.com/ds-project-s3/ds-files/README.md" 
}
```

If azure function do correctly, you will see this response 

```json
"Complete Process of url https://s3.ap-northeast-2.amazonaws.com/ds-project-s3/ds-files/test.txt"
```
