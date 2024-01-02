import splitfolders

'''
    INPUT : Specify path to root directory containing subdirectory (named as labels)
    OUTPUT : Path to output directory
'''
# Example 
#input_folder = "/workspace/data_DIR/gaussian_filtered_images/gaussian_filtered_images"
#output_folder = "/workspace/data_DIR/gaussian_filtered_images/gaussian_filtered_images_processed"

splitfolders.ratio(input_folder, output_folder, seed = 42, ratio=(.7,.1,.2))