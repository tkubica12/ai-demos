Overriding: out_dir = azure_docs_out
Overriding: num_samples = 1
Overriding: max_new_tokens = 300
Overriding: start = FILE:prompts/basic.txt
number of parameters: 123.59M
No meta.pkl found, assuming GPT-2 encodings...
In order to configure two Azure Virtual Networks in two different regions to communicate with each other you need to  enable *HTTP configuration* to connect to the Azure Database for MariaDB server in three different regions. This configuration configures connectivity between the two data centers to ensure connectivity between the two data centers.

When the server is closed, the server sends a response to the client. The connection is returned to the server.

## How to connect

[!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]

## Prerequisites

Before you can connect to your database server, you need to connect to your server.

Install the [Azure Database for MariaDB server](/azure/azure-database/install-Azure-portal) extension. Install `mysql` extension, see [Install, set up, and configure a server](/azure/azure-database/install-azure-cli) for Azure Database for MariaDB Server and *Azure PowerShell*, as shown in the following example:

```powershell-interactive
Connect-AzAccount
Select-AzSubscription -Subscription 00000000-0000-0000-0000-000000000000
```

## Connect server options

Use the following request to connect to your server, including firewall rules or settings associated with your server.

```azurepowershell-interactive
$
---------------
