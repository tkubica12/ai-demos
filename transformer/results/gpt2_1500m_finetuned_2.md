In order to configure two Azure Virtual Networks in two different regions to communicate with each other you need to   *download the Azure Virtual Networks created in the other region* 
      *create a second cluster in the other region* 
      *then create a virtual private network between the two clusters** | 
      *then connect the two clusters* 
      *then create an Azure virtual network between each cluster* 
      *then create a firewall between the two clusters* 
      *then configure the network between the cluster services* 
      

**Fetch Azure Virtual Networks CSV: https://azure.microsoft.com/azure/powershell/azure-cluster-configuration/azure-virtual-network-configuration-csv.json

## Step 1: Download Azure Virtual Network CSV (requires a free Azure web app license)
Sign in to your Azure web app at https://azure.microsoft.com/ and then select <Azure portal name>. Then select your region from the <Region name> drop-down menu. Then select the <Region> node in the <Virtual networks>" section. Then select the <Virtual networks>" section of the page.

Then select <Download as CSV> from the menu at the top of the page. And then select <Download CSV> on the next screen.

Here are the steps to follow:
---------------
