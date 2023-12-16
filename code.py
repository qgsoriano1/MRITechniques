import SimpleITK as sitk
import matplotlib.pyplot as plt

def load_image(file_path):
    try:
        image = sitk.ReadImage(file_path)
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def display_image(image, title):
    plt.imshow(sitk.GetArrayViewFromImage(image), cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def smooth_image(image, sigma=1.0):
    smoothed_image = sitk.SmoothingRecursiveGaussian(image, sigma)
    return smoothed_image

def segment_image(image):
    # Example: Threshold-based segmentation
    binary_image = sitk.BinaryThreshold(image, lowerThreshold=100, upperThreshold=500)
    return binary_image

def main():
    # Replace 'your_mri_image.nii.gz' with the path to your MRI image
    file_path = 'C:\\Users\\GSori\\OneDrive\\Documents\\4thYear\\DSPA\\MRITechniques\\assets\\brain-lesion_T1w.nii.gz'

    # Load MRI image
    mri_image = load_image(file_path)

    if mri_image is not None:
        # Display original image
        display_image(mri_image, 'Original MRI Image')

        # Smooth the image
        smoothed_image = smooth_image(mri_image)
        display_image(smoothed_image, 'Smoothed MRI Image')

        # Segment the image
        segmented_image = segment_image(mri_image)
        display_image(segmented_image, 'Segmented MRI Image')

if __name__ == "__main__":
    main()
