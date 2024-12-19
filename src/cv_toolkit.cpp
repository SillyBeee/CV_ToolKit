#include <QApplication>
#include <QMainWindow>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QComboBox>
#include <QSpinBox>
#include <QDoubleSpinBox>
#include <QImage>
#include <QPixmap>
#include <QGraphicsView>
#include <QGraphicsScene>
#include <QFileDialog>
#include <QMessageBox>
#include <QMouseEvent>
#include <opencv2/opencv.hpp>

class CVToolbox : public QMainWindow {
    Q_OBJECT

public:
    CVToolbox(QWidget *parent = nullptr);
    ~CVToolbox();

protected:
    void mouseMoveEvent(QMouseEvent *event) override;

private slots:
    void updateUI();
    void loadImage();
    void applyProcessing();
    void updateImageView();
    void toggleColorDisplayMode();

private:
    QComboBox *functionComboBox;
    QSpinBox *kernelSizeSpinBox;
    QDoubleSpinBox *sigmaSpinBox;
    QSpinBox *thresholdSpinBox;
    QSpinBox *maxValueSpinBox;
    QDoubleSpinBox *gammaSpinBox;
    QLabel *colorLabel;
    QPushButton *colorModeButton;
    QGraphicsView *imageView;
    QGraphicsScene *imageScene;
    QVBoxLayout *parameterLayout;

    cv::Mat originalImage; // Store the original image
    cv::Mat image;         // Store the currently processed image
    bool displayHSV;       // Toggle between RGB and HSV display mode
};

CVToolbox::CVToolbox(QWidget *parent) : QMainWindow(parent), displayHSV(false) {
    // Main layout
    auto *mainWidget = new QWidget;
    auto *mainLayout = new QVBoxLayout;

    // Top layout for function selection
    auto *topLayout = new QHBoxLayout;
    QLabel *functionLabel = new QLabel("Select Function:");
    functionComboBox = new QComboBox;
    functionComboBox->addItems({"Gaussian Blur", "Median Blur", "Denoising", "Color Picker", "Remove Watermark", "Thresholding", "Gamma Correction"});
    connect(functionComboBox, &QComboBox::currentTextChanged, this, &CVToolbox::updateUI);

    topLayout->addWidget(functionLabel);
    topLayout->addWidget(functionComboBox);
    mainLayout->addLayout(topLayout);

    // Parameter layout
    parameterLayout = new QVBoxLayout;
    mainLayout->addLayout(parameterLayout);

    // Image view
    imageScene = new QGraphicsScene(this);
    imageView = new QGraphicsView(imageScene);
    mainLayout->addWidget(imageView);

    // Color label for real-time color display
    colorLabel = new QLabel("Color: N/A");
    colorModeButton = new QPushButton("Switch to HSV");
    connect(colorModeButton, &QPushButton::clicked, this, &CVToolbox::toggleColorDisplayMode);
    auto *colorLayout = new QHBoxLayout;
    colorLayout->addWidget(colorLabel);
    colorLayout->addWidget(colorModeButton);
    mainLayout->addLayout(colorLayout);

    // Button layout
    auto *buttonLayout = new QHBoxLayout;
    QPushButton *loadButton = new QPushButton("Load Image");
    QPushButton *applyButton = new QPushButton("Apply");
    buttonLayout->addWidget(loadButton);
    buttonLayout->addWidget(applyButton);

    connect(loadButton, &QPushButton::clicked, this, &CVToolbox::loadImage);
    connect(applyButton, &QPushButton::clicked, this, &CVToolbox::applyProcessing);

    mainLayout->addLayout(buttonLayout);

    mainWidget->setLayout(mainLayout);
    setCentralWidget(mainWidget);
    setWindowTitle("CV Toolbox");
    resize(800, 600);

    updateUI(); // Initialize UI elements based on the default function
}

CVToolbox::~CVToolbox() {
}

void CVToolbox::updateUI() {
    // Clear existing parameters
    QLayoutItem *child;
    while ((child = parameterLayout->takeAt(0)) != nullptr) {
        delete child->widget();
        delete child;
    }

    QString function = functionComboBox->currentText();
    if (function == "Gaussian Blur") {
        QLabel *kernelLabel = new QLabel("Kernel Size:");
        kernelSizeSpinBox = new QSpinBox;
        kernelSizeSpinBox->setRange(1, 31);
        kernelSizeSpinBox->setValue(5);

        QLabel *sigmaLabel = new QLabel("Sigma:");
        sigmaSpinBox = new QDoubleSpinBox;
        sigmaSpinBox->setRange(0.1, 10.0);
        sigmaSpinBox->setValue(1.0);

        parameterLayout->addWidget(kernelLabel);
        parameterLayout->addWidget(kernelSizeSpinBox);
        parameterLayout->addWidget(sigmaLabel);
        parameterLayout->addWidget(sigmaSpinBox);
    } else if (function == "Median Blur") {
        QLabel *kernelLabel = new QLabel("Kernel Size:");
        kernelSizeSpinBox = new QSpinBox;
        kernelSizeSpinBox->setRange(1, 31);
        kernelSizeSpinBox->setValue(5);
        parameterLayout->addWidget(kernelLabel);
        parameterLayout->addWidget(kernelSizeSpinBox);
    } else if (function == "Denoising") {
        QLabel *strengthLabel = new QLabel("Denoising Strength:");
        sigmaSpinBox = new QDoubleSpinBox;
        sigmaSpinBox->setRange(0.1, 10.0);
        sigmaSpinBox->setValue(1.0);
        parameterLayout->addWidget(strengthLabel);
        parameterLayout->addWidget(sigmaSpinBox);
    } else if (function == "Color Picker") {
        QLabel *infoLabel = new QLabel("Hover over the image to pick a color.");
        parameterLayout->addWidget(infoLabel);
    } else if (function == "Remove Watermark") {
        QLabel *infoLabel = new QLabel("Please load the mask or define the watermark region manually.");
        parameterLayout->addWidget(infoLabel);
    } else if (function == "Thresholding") {
        QLabel *thresholdLabel = new QLabel("Threshold Value:");
        thresholdSpinBox = new QSpinBox;
        thresholdSpinBox->setRange(0, 255);
        thresholdSpinBox->setValue(128);

        QLabel *maxValueLabel = new QLabel("Max Value:");
        maxValueSpinBox = new QSpinBox;
        maxValueSpinBox->setRange(0, 255);
        maxValueSpinBox->setValue(255);

        parameterLayout->addWidget(thresholdLabel);
        parameterLayout->addWidget(thresholdSpinBox);
        parameterLayout->addWidget(maxValueLabel);
        parameterLayout->addWidget(maxValueSpinBox);
    } else if (function == "Gamma Correction") {
        QLabel *gammaLabel = new QLabel("Gamma Value:");
        gammaSpinBox = new QDoubleSpinBox;
        gammaSpinBox->setRange(0.1, 5.0);
        gammaSpinBox->setValue(1.0);

        parameterLayout->addWidget(gammaLabel);
        parameterLayout->addWidget(gammaSpinBox);
    }
}

void CVToolbox::loadImage() {
    QString fileName = QFileDialog::getOpenFileName(this, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp)");
    if (!fileName.isEmpty()) {
        originalImage = cv::imread(fileName.toStdString());
        if (originalImage.empty()) {
            QMessageBox::critical(this, "Error", "Failed to load the image.");
            return;
        }
        image = originalImage.clone();
        updateImageView();
    }
}

void CVToolbox::applyProcessing() {
    if (originalImage.empty()) {
        QMessageBox::warning(this, "Warning", "No image loaded.");
        return;
    }

    QString function = functionComboBox->currentText();
    image = originalImage.clone(); // Reset to the original image before processing
    cv::Mat processedImage;

    try {
        if (function == "Gaussian Blur") {
            int kernelSize = kernelSizeSpinBox->value();
            double sigma = sigmaSpinBox->value();
            cv::GaussianBlur(image, processedImage, cv::Size(kernelSize, kernelSize), sigma);
        } else if (function == "Median Blur") {
            int kernelSize = kernelSizeSpinBox->value();
            if (kernelSize % 2 == 0) kernelSize += 1; // Ensure kernel size is odd
            cv::medianBlur(image, processedImage, kernelSize);
        } else if (function == "Denoising") {
            double strength = sigmaSpinBox->value();
            cv::fastNlMeansDenoisingColored(image, processedImage, static_cast<float>(strength));
        } else if (function == "Thresholding") {
            int thresholdValue = thresholdSpinBox->value();
            int maxValue = maxValueSpinBox->value();
            cv::threshold(image, processedImage, thresholdValue, maxValue, cv::THRESH_BINARY);
        } else if (function == "Gamma Correction") {
            double gammaValue = gammaSpinBox->value();
            cv::Mat lut(1, 256, CV_8UC1);
            for (int i = 0; i < 256; i++) {
                lut.at<uchar>(i) = cv::saturate_cast<uchar>(pow(i / 255.0, gammaValue) * 255.0);
            }
            cv::LUT(image, lut, processedImage);
        } else if (function == "Remove Watermark") {
            cv::Mat mask = cv::Mat::zeros(image.size(), CV_8U);
            cv::rectangle(mask, cv::Point(50, 50), cv::Point(200, 100), cv::Scalar(255), -1);
            cv::inpaint(image, mask, processedImage, 3, cv::INPAINT_TELEA);
        }

        if (!processedImage.empty()) {
            image = processedImage;
            updateImageView();
        }
    } catch (const cv::Exception &e) {
        QMessageBox::critical(this, "Error", e.what());
    }
}

void CVToolbox::updateImageView() {
    if (image.empty()) return;
    cv::Mat rgbImage;
    cv::cvtColor(image, rgbImage, cv::COLOR_BGR2RGB);
    QImage qImage((uchar *)rgbImage.data, rgbImage.cols, rgbImage.rows, rgbImage.step, QImage::Format_RGB888);
    imageScene->clear();
    imageScene->addPixmap(QPixmap::fromImage(qImage));
    imageView->fitInView(imageScene->itemsBoundingRect(), Qt::KeepAspectRatio);
}

void CVToolbox::mouseMoveEvent(QMouseEvent *event) {
    if (originalImage.empty() || functionComboBox->currentText() != "Color Picker") return;

    QPointF point = imageView->mapToScene(event->pos());
    int x = static_cast<int>(point.x());
    int y = static_cast<int>(point.y());

    if (x >= 0 && x < originalImage.cols && y >= 0 && y < originalImage.rows) {
        cv::Vec3b color = originalImage.at<cv::Vec3b>(y, x);
        if (displayHSV) {
            cv::Mat bgr(1, 1, CV_8UC3, cv::Scalar(color[0], color[1], color[2]));
            cv::Mat hsv;
            cv::cvtColor(bgr, hsv, cv::COLOR_BGR2HSV);
            cv::Vec3b hsvColor = hsv.at<cv::Vec3b>(0, 0);
            colorLabel->setText(QString("HSV: H=%1 S=%2 V=%3")
                                .arg(hsvColor[0])
                                .arg(hsvColor[1])
                                .arg(hsvColor[2]));
        } else {
            colorLabel->setText(QString("RGB: R=%1 G=%2 B=%3")
                                .arg(color[2])
                                .arg(color[1])
                                .arg(color[0]));
        }
    } else {
        colorLabel->setText("Color: N/A");
    }
}

void CVToolbox::toggleColorDisplayMode() {
    displayHSV = !displayHSV;
    colorModeButton->setText(displayHSV ? "Switch to RGB" : "Switch to HSV");
}
int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    CVToolbox toolbox;
    toolbox.show();
    return app.exec();
}
#include "cv_toolkit.moc"