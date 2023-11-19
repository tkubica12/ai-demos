In order to configure two Azure Virtual Networks in two different regions to communicate with each other you need to  enable *HTTP configuration* to connect to the Azure Database for MariaDB server in three different regions. This configuration configures connectivity between the two data centers to ensure connectivity between the two data centers.

When the server is closed, the server sends a response to the client. The connection is returned to the server.

## How to connect

[!INCLUDE [applies-to-postgresql-flexible-server](../includes/applies-to-postgresql-flexible-server.md)]

## Prerequisites

Before you can connect to your database server, you need to connect to your server.

Install the [Azure Database for MariaDB server](/azure/azure-database/quickstart-create-server-database-portal) and supply a range of subnets to connect to the server.

## Read data

The server can be read data from the server using Read Data.

### [Portal](#tab/Azure_Portal)

In the Azure portal, use the following steps:

1. Open the Azure Database for MariaDB server.

2. Select **Server Parameters** from the settings bar at the top left, select **General Purpose**, **General Purpose**, **General Purpose**, **General Purpose settings**, or **General Purpose settings** options.

3. In the **General
---------------
