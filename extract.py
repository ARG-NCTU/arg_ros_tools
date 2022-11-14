import os
import cv2
from cv_bridge import CvBridge
import rosbag

class arg_bag_extracter:
    def __init__(self, bag_file, output_dir, image_topic): 
        self.bag_file = bag_file
        self.bag = rosbag.Bag(self.bag_file, "r")
        self.output_dir = output_dir
        self.image_topic = image_topic

    def extract(self):
        bridge = CvBridge()
        count = 0
        for topic, msg, t in self.bag.read_messages(topics=[self.image_topic]):
            cv_img = bridge.imgmsg_to_cv2(msg, "bgr8")
            cv2.imwrite(os.path.join(self.output_dir, "color%06i.jpg" % count), cv_img)
            count += 1
        self.bag.close()
        print("done, count is "+ str(count) + " and output to " + self.output_dir)

my_dirs = ['1112_1151/', '1112_1130/', '1112_1256/', '1112_1253/', '1112_1257/', '1112_1152/', '1112_1148/']
path = "/home/arg/Ezra/"
image_topic = "/wamv/zed_mid/zed_node/rgb/image_rect_color"
for my_dir in my_dirs:
    numbers = os.listdir(path+my_dir)
    for number in numbers:
        bag_name = path+my_dir+number[:28]
        print(bag_name)
        bag_file = bag_name + ".bag" 
        print(bag_file)
        output_dir = bag_name + "/"
        print(output_dir)
        os.mkdir(output_dir)
        extracter = arg_bag_extracter(bag_file, output_dir, image_topic)
        extracter.extract()

