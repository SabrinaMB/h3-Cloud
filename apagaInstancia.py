import openstack

openstack.enable_logging(debug=True)
print("conectando\n\n\n\n\n\n\n\n")
conn = openstack.connect(
    region_name='RegionOne',
    auth=dict(
        auth_url='http://192.168.15.51:5000/v3',
        username='Sabrina',
        password='cloude',
        project_domain_name='admin_domain',
        user_domain_name='admin_domain'),
   # compute_api_version='3',
    identity_interface='internal')
print("deleting server \n\n\n\n\n\n\n\n\n")
server = conn.compute.find_server("my-server")
conn.delete_server(server)
