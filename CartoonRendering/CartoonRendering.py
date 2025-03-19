import cv2

# ������ ����
def DetectEdges(image):

    # BGR �̹���(�� ���� ä��)�� GRAY �̹���(����ä��)�� ��ȯ�Ѵ�
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # ���ʿ��� ����� ���̱� ���� median blur ����
    gray = cv2.medianBlur(gray, 5)
    
    return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)


# bilateral filter�� �����Ͽ� �������� �����ϸ� �̹����� �ε巴�� �����
def BlurImgae(image):
    return cv2.bilateralFilter(img, 9, 300, 300)


# �̹��� �ҷ�����
img = cv2.imread('image.jpg')

edges = DetectEdges(img)
blured = BlurImgae(img)

# ó���� �̹����� �������� ��ģ��
output = cv2.bitwise_and(blured, blured, mask=edges)

# Display the cartoon image
cv2.imshow("CartoonRendering", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

