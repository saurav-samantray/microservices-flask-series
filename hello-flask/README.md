# Hello Flask
A basic flask application to demonstrate how to create and start a flask restful application and test a sample request/response

<br />

## Virtual Env setup
### Create Virtual Environment
```
python -m venv venv
```

### Activating Virtual Environment
```
venv\Scripts\activate
```
### Deactivating Virtual Environment
```
deactivate
```
<br />

## Installing the requirements
```
pip install -r requirements.txt
```

## Possible erros
### Running activate/deactive script via visual studio terminal - <b>cannot be loaded 
because running scripts is disabled on this system.</b>

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Revert back once done
```
Set-ExecutionPolicy Restricted
```