In order to configure two Azure Virtual Networks in two different regions to communicate with each other you need to  Install Azure Web Services  and we need to add  many-access authentication rules to our VM.
An example of how to do this would be to test .NET 8.0 and .NET Core 5.0 deployments.
In the wizard, see "Add an Azure Active Directory Server" , we set UPnP to our new virtual environment as shown above.
Add an In-Memory Windows Distributed Machine (DDLMS) Deployment
Connect to our virtual local environment and create an Azure Active Directory Server (AD DS).
Create an Azure Active Directory Server (AD DS) in this Azure domain.
Click Create.
Make sure to set up Windows PowerShell to participate in this step.
First, create a new Active Directory Service. For more information about Deployment and Deployment cmdlets in Windows PowerShell see This site, see How to Use Microsoft's Deployment Project, and Read more .
Now use the Azure Active Directory Services to create two virtual network devices's .NET domain, which will communicate with one another.
With the AD DS created, the 2nd virtual network device will communicate with one of the virtual network devices in the cluster. Set up a Windows PowerShell role during this time so it implements the Active Directory Role Service, and you'll be able to use the AD DS to deploy to both regions.
Make sure that the Active Directory Service needs to be running on both servers.
New in PowerShell 3.5
Add
---------------
