# import os
# os.system("cls")

# os.system("echo File Recovery Script")
# os.system("For Programing Wonders")
# os.system("echo The list of devices is")
# os.system("wmic logicaldisk get name")
# os.system("echo enter the device to be used")
# devname = input("")
# imgname = input("Enter the image name \n")
# os.system("diskpart if="+devname+" of=" + imgname +" bs=512")
# os.system("echo showing inode number of files")
# os.system("fls "+ imgname)
# inodeno = input("Enter the inode of the deleted file ")
# os.system("istat "+ imgname + " " + inodeno )
# os.system("echo the contents of the recovered file are")
# os.system("icat "+ imgname +" "+ inodeno)
# os.system("echo enter the name of the file where data to be stored with extension")
# newfile = input("")
# os.system("icat "+ imgname +" "+ inodeno +" > "+ newfile )
# os.system("echo the contents of the file are")
# os.system("cat "+ newfile )


# import os
# os.system("clear")
# os.system("echo File Recovery Script")
# os.system("For Programing Wonders")
# os.system("echo The list of devices is")
# os.system("diskutil list")
# os.system("echo enter the device to be used")
# devname = input("")
# imgname = input("Enter the image name \n")
# os.system("dd if="+devname+" of=" + imgname +" bs=512")
# os.system("echo showing inode number of files")
# os.system("fls "+ imgname)
# inodeno = input("Enter the inode of the deleted file ")
# os.system("istat "+ imgname + " " + inodeno )
# os.system("echo the contents of the recovered file are")
# os.system("icat "+ imgname +" "+ inodeno)
# os.system("echo enter the name of the file where data to be stored with extension")
# newfile = input("")
# os.system("icat "+ imgname +" "+ inodeno +" > "+ newfile )
# os.system("echo the contents of the file are")
# os.system("cat "+ newfile )

import subprocess
import os

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr.decode()}")

def main():
    # Clear the terminal screen
    os.system("cls")
    
    # Display script title
    print("File Recovery Script")
    print("For Programming Wonders")
    
    # List devices
    print("The list of devices is:")
    run_command("wmic logicaldisk get name")  # List drives on Windows
    
    # Get the device name and image name from user
    devname = input("Enter the device to be used (e.g., C: or D:): ")
    imgname = input("Enter the image name: \n")
    
    # Create disk image using dd (you need dd for Windows)
    print(f"Creating disk image from {devname} to {imgname}")
    run_command(f"dd if={devname} of={imgname} bs=512")  # Assuming dd is installed for Windows
    
    # Show inode numbers of files
    print("Showing inode number of files")
    run_command(f"fls {imgname}")
    
    # Get the inode number of the deleted file
    inodeno = input("Enter the inode of the deleted file: ")
    
    # Show metadata of the file
    print("File information:")
    run_command(f"istat {imgname} {inodeno}")
    
    # Show the contents of the recovered file
    print("The contents of the recovered file are:")
    run_command(f"icat {imgname} {inodeno}")
    
    # Get the filename where the recovered data should be stored
    newfile = input("Enter the name of the file where data to be stored with extension: ")
    
    # Save the recovered file to a new file
    print(f"Saving the recovered data to {newfile}")
    run_command(f"icat {imgname} {inodeno} > {newfile}")
    
    # Display the contents of the saved file
    print("The contents of the new file are:")
    run_command(f"type {newfile}")  # Using 'type' instead of 'cat' on Windows

if __name__ == "__main__":
    main()
