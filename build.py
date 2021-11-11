def get_input(prompt: str = ": ") -> str:
    confirm = None
    while not confirm:
        response = input(prompt)
        confirm = input(f"{response}? (y/n)")
        if confirm.lower() != "y":
            confirm = None
    return response


mgmt_server_ip = get_input("Enter the mgmt server IP: ")
old_version = get_input("Enter the current mgmt version: ")
new_version = get_input("Enter the new mgmt version: ")
rc = get_input("Enter the rc: ")
if rc:
    rc = f"-rc{rc}"

with open("inventory.ini", "w") as inventory_file:
    inventory_file.write("[all:vars]\n")
    inventory_file.write("ansible_ssh_user=ld-admin\n")
    inventory_file.write("ansible_ssh_private_key_file=/tmp/dynamic-keypair.pem\n")
    inventory_file.write(f"old_version={old_version}\n")
    inventory_file.write(f"new_version={new_version}\n")
    inventory_file.write(f"rc={rc}\n")
    inventory_file.write("\n")
    inventory_file.write("[mgmt]\n")
    inventory_file.write(mgmt_server_ip)
