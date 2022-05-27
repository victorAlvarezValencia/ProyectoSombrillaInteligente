import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory , JointTrajectoryPoint, MultiDOFJointTrajectory

class Trajectory_publisher(Node):
	
    def __init__(self):
        super().__init__('trajectory_publsiher_node')
        publish_topic = "/joint_trajectory_controller/joint_trajectory"
        self.trajectory_publihser = self.create_publisher(JointTrajectory,publish_topic, 10)
        timer_period = 7
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.joints = ['joint1','joint2','joint3']
        self.goal_positions = [0.5,0.5,0.5]
        self.goal_positions1 = [0.2,0.6,0.4]
        self.goal_positions2 = [0.3,0.2,0.8]


    def timer_callback(self):
        robotinRutas_trajectory_msg = JointTrajectory()
        robotinRutas_trajectory_msg.joint_names = self.joints
        ## creating a point
        point = JointTrajectoryPoint()
        point.positions = self.goal_positions
        point.time_from_start = Duration(sec=2)
        
        robotinRutas_trajectory_msg.points.append(point) 
        ## adding newly created point into trajectory message
        point_1 = JointTrajectoryPoint()
        point_1.positions = self.goal_positions1
        point_1.time_from_start = Duration(sec=5)
        
        robotinRutas_trajectory_msg.points.append(point_1) 
        
        point_2 = JointTrajectoryPoint()
        point_2.positions = self.goal_positions2
        point_2.time_from_start = Duration(sec=7)
        
    
        robotinRutas_trajectory_msg.points.append(point_2)
                 
        self.trajectory_publihser.publish(robotinRutas_trajectory_msg)
        
        
       

def main(args=None):


    rclpy.init(args=args)
    joint_trajectory_object = Trajectory_publisher()

    rclpy.spin(joint_trajectory_object)
    joint_trajectory_object.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
