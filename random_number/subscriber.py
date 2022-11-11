import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64


class RandomNumberSubscriber(Node):

    def __init__(self):
        super().__init__('random_number_subscriber')
        self.subscription = self.create_subscription(Int64, "/number", self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info("Recieved a random number: %d" % msg.data)


def main(args=None):
    rclpy.init(args=args)

    random_number_subscriber = RandomNumberSubscriber()

    rclpy.spin(random_number_subscriber)
    random_number_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()