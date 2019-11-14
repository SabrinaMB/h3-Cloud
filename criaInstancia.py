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
print("uploading image \n\n\n\n\n\n\n\n\n")
# Upload an image to the cloud
image = conn.get_image('bionic')

# Find a flavor with at least 512M of RAM
#flavor = conn.flavors()

flavors = []
for flavor in conn.compute.flavors():
    if (dict(flavor))['ram'] >= 512:
        flavors.append(flavor)
# Find a flavor with at least 512M of RAM
#flavor = { 'id' : '5cf64088-893b-46b5-9bb1-ee020277635d'}
flavor = flavors[0]
# Boot a server, wait for it to boot, and then do whatever is needed
# to get a public ip for it.
conn.create_server('my-server', image=image, flavor=flavor, key_name="sabrina")
