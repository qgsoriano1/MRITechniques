import SimpleITK as sitk
import matplotlib.pyplot as plt

def load_image(file_path):
    try:
        image = sitk.ReadImage(file_path)
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def display_image_slice(image, slice_number, title):
    slice_2d = sitk.GetArrayViewFromImage(image)[slice_number, :, :]
    plt.imshow(slice_2d, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def smooth_image(image, sigma=1.0):
    smoothed_image = sitk.SmoothingRecursiveGaussian(image, sigma)
    return smoothed_image

def segment_image(image):
    binary_image = sitk.BinaryThreshold(image, lowerThreshold=100, upperThreshold=500)
    return binary_image

def main():
    file_path = r'C:\Users\GSori\OneDrive\Documents\4thYear\DSPA\MRITechniques\assets\wash-120_sub-001_T1w.nii.gz'
    mri_image = load_image(file_path)

    if mri_image is not None:
        display_image_slice(mri_image, slice_number=100, title='Original MRI Image')
        smoothed_image = smooth_image(mri_image)
        display_image_slice(smoothed_image, slice_number=100, title='Smoothed MRI Image')
        segmented_image = segment_image(mri_image)
        display_image_slice(segmented_image, slice_number=100, title='Segmented MRI Image')

if __name__ == "__main__":
    main()
