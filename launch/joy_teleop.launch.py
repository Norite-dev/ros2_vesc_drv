from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(package="joy", executable="joy_node", name="joy_node"),
            Node(
                package="teleop_twist_joy",
                executable="teleop_node",
                parameters=[{
                    'require_enable_button': False, 
                    'axis_linear.x':1, 
                    'scale_linear.x': 1.0, 
                    'axis_angular.yaw':3, 
                    'scale_angular.yaw': 1.0
                }],
            ),
        ]
    )
