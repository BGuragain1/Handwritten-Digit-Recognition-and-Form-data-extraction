from ScanForm.models import ClientDetails

def insertData(data,id):
    
    personal = data["personal_info"]
    nominee = data["nominee_info"]
    temp = data["temporary_address"]
    perm = data["permanent_address"]

    client = ClientDetails(
        user_id=id,
        
    )

    client.save()
 

def updateData(id):
    client = ClientDetails.objects.get(user_id=id)

    client.first_name = 'Jane'
    client.save()

    return

def deleteClient(id):
    client = ClientDetails.objects.get(user_id=id)
    client.delete()
    return
