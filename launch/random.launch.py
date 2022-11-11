from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='random_number',
            namespace='random_number1',
            executable='publisher',
        ),
        Node(
            package='random_number',
            namespace='random_number2',
            executable='subscriber',
        ),
    ])