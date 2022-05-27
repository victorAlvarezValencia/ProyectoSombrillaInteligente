import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory , JointTrajectoryPoint, MultiDOFJointTrajectory
from math import*
from operator import inv
from xmlrpc.client import Transport
from numpy import append, concatenate, matrix #Forma facil 
import numpy as np
from numpy import*


class Trajectory_publisher(Node):

    def __init__(self):
        super().__init__('trajectory_publsiher_node')
        publish_topic = "/joint_trajectory_controller/joint_trajectory"
        self.trajectory_publihser = self.create_publisher(JointTrajectory,publish_topic, 10)
        timer_period = 7
        self.timer = self.create_timer(timer_period, self.timer_callback)
        CallAngulos = self.angulosinv()
        θ1= CallAngulos[0]
        θ2 = CallAngulos[1]
        θ3 = CallAngulos[2]
        θ11 = CallAngulos[3]
        θ21 = CallAngulos[4]
        θ31 = CallAngulos[5]
        θ12= CallAngulos[6]
        θ22 = CallAngulos[7]
        θ32 = CallAngulos[8]
        θ13= CallAngulos[9]
        θ23 = CallAngulos[10]
        θ33 = CallAngulos[11]
        θ14= CallAngulos[12]
        θ24 = CallAngulos[13]
        θ34 = CallAngulos[14]
        self.joints = ['joint1','joint2','joint3']
        self.goal_positions = [θ1,θ2,θ3]
        self.goal_positions1 = [θ11,θ21,θ31]
        self.goal_positions2 = [θ12,θ22,θ32]
        self.goal_positions3 = [θ13,θ23,θ33]
        self.goal_positions4 = [θ14,θ24,θ34]



    def angulosinv(self):
        Px=6
        Py=-1
        Pz=4
        l2=5
        l3=5
        θ1=arctan2(Py,Px)
        θ2=arctan2(Px*cos(θ1)+Py*sin(θ1),Pz)
        cosq3=(Px**2+Py**2+Pz**2-l2**2-l3**2)/(2*l2**2*l3**2)
        sinq3=-sqrt(1-cosq3**2)
        θ3=arctan2(sinq3,cosq3)
        
        Px1=-5
        Py1=-1
        Pz1=4
        l21=5
        l31=5
        θ11=arctan2(Py1,Px1)
        θ21=arctan2(Px1*cos(θ11)+Py*sin(θ11),Pz1)
        cosq3=(Px1**2+Py1**2+Pz1**2-l21**2-l31**2)/(2*l21**2*l31**2)
        sinq3=sqrt(1-cosq3**2)
        θ31=arctan2(sinq3,cosq3)
        
        Px2=-5
        Py2=-2
        Pz2=3
        l22=5
        l32=5
        θ12=arctan2(Py2,Px2)
        θ22=arctan2(Px2*cos(θ1)+Py2*sin(θ1),Pz2)
        cosq3=(Px2**2+Py2**2+Pz2**2-l22**2-l32**2)/(2*l22**2*l32**2)
        sinq3=-sqrt(1-cosq3**2)
        θ32=arctan2(sinq3,cosq3)
        
        
        Px3=-5
        Py3=-1
        Pz3=4
        l23=5
        l33=5
        θ13=arctan2(Py3,Px3)
        θ23=arctan2(Px3*cos(θ1)+Py3*sin(θ1),Pz3)
        cosq3=(Px3**2+Py3**2+Pz3**2-l23**2-l33-3**2)/(2*l23**2*l33**2)
        sinq3=-sqrt(1-cosq3**2)
        θ33=arctan2(sinq3,cosq3)
 
        Px4=6
        Py4=-1
        Pz4=4
        l24=5
        l34=5
        θ14=arctan2(Py3,Px3)
        θ24=arctan2(Px3*cos(θ1)+Py3*sin(θ1),Pz3)
        cosq3=(Px4**2+Py4**2+Pz4**2-l24**2-l34-3**2)/(2*l24**2*l34**2)
        sinq3=-sqrt(1-cosq3**2)
        θ34=arctan2(sinq3,cosq3)
  
        return [θ1, θ2, θ3, θ11, θ21, θ31, θ12, θ22, θ32, θ13, θ23, θ33, θ14, θ24, θ34]

	
    def timer_callback(self):
        robotinRutas_trajectory_msg = JointTrajectory()
        robotinRutas_trajectory_msg.joint_names = self.joints
        ## creating a point
        point = JointTrajectoryPoint()
        point.positions = self.goal_positions
        point.time_from_start = Duration(sec=4)
        
        robotinRutas_trajectory_msg.points.append(point) 
        ## adding newly created point into trajectory message
        point_1 = JointTrajectoryPoint()
        point_1.positions = self.goal_positions1
        point_1.time_from_start = Duration(sec=10)
        
        robotinRutas_trajectory_msg.points.append(point_1) 
        
        point_2 = JointTrajectoryPoint()
        point_2.positions = self.goal_positions2
        point_2.time_from_start = Duration(sec=14)
        
        robotinRutas_trajectory_msg.points.append(point_2)
        
        point_3 = JointTrajectoryPoint()
        point_3.positions = self.goal_positions2
        point_3.time_from_start = Duration(sec=15)
        
        robotinRutas_trajectory_msg.points.append(point_3)
        
        point_4 = JointTrajectoryPoint()
        point_4.positions = self.goal_positions2
        point_4.time_from_start = Duration(sec=17)
        
        robotinRutas_trajectory_msg.points.append(point_4)
        
        self.trajectory_publihser.publish(robotinRutas_trajectory_msg)
        


def main(args=None):


    rclpy.init(args=args)
    joint_trajectory_object = Trajectory_publisher()

    rclpy.spin(joint_trajectory_object)
    joint_trajectory_object.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
