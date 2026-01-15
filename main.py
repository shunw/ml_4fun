import scipy.io as sio

def main():
    print("Hello from ev-energy!")


if __name__ == "__main__":
    main()

    # 1. Specify the file path
    file_path = 'data/algae.mat'

    # 2. Load the .mat file
    # The 'muf' variable will be a dictionary
    muf = sio.loadmat(file_path)

    # 3. Explore the contents (optional, but helpful)
    # Print the keys to see the variable names stored in the file
    print(muf.keys())

    # 4. Access a specific variable
    # Replace 'variable_name' with one of the keys found in step 3
    data_variable = muf['ans']
    print (data_variable)

    # Example of accessing and flattening an array
    # mu = muf.get('mu') # or use dictionary access
    # mu = mu.flatten()
