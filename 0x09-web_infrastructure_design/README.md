Web Infrastructure Design
Authors: Noah Owens & Abuto I

This repository contains diagrams and documentation for web infrastructure design projects completed by Noah Owens and Abuto I.

Tasks
0. Simple web stack
A simple web stack was designed with 1 server running Nginx as the web server, an application server, application files, and a MySQL database. The infrastructure diagram and documentation explains the role of each component.

1. Distributed web infrastructure
A distributed infrastructure was designed with 3 servers - 2 web servers running Nginx, 1 application server, 1 load balancer, 1 set of application files, and a MySQL database. The diagram and documentation outlines the reasons for adding additional components like the load balancer, as well as issues like single points of failure.

2. Secured and monitored web infrastructure
The distributed infrastructure was enhanced with security and monitoring. 3 firewalls were added, a SSL certificate for serving HTTPS traffic, and 3 monitoring clients. The documentation explains the purpose of each additional component.

3. Scale up
The infrastructure was scaled up with an additional server, load balancer configured as a cluster, and split components on their own servers. The documentation outlines the reasons for scaling.

In each task, diagrams were created to visualize the infrastructure, and documentation was added to explain the design and issues. The documentation and diagrams were created collaboratively by Noah Owens and Abuto I to demonstrate understanding of system infrastructure design
