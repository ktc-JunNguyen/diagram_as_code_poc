from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import ECS
from diagrams.aws.network import ELB
from diagrams.aws.network import ALB
from diagrams.aws.network import CF
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.aws.devtools import Codepipeline, Codebuild
from diagrams.aws.management import Cloudwatch
from diagrams.aws.security import IAMRole
from diagrams.aws.general import Users
from diagrams.aws.database import RDS
from diagrams.c4 import Container

with Diagram("Kinto", show=False, direction="TB"):
    users = Users("Users")

    with Cluster("Browser"):
        frontend = Container(
            name="Goku Frontend"
        )

    with Cluster("AWS Cloud"):

        
        with Cluster("Public subnet"):
            alb = ALB("Load Balancer")

        with Cluster("Private subnet"):
            rds = RDS("goku")
            with Cluster("goku-backend"):
                ecs = ECS("deal")
                ecs = ECS("price")
                ecs = ECS("conversion")
                ecs = ECS("core")
    
    users >> frontend
    frontend >> alb 

    alb >> ecs
    ecs >> rds
    rds >> ecs
    ecs >> alb

    alb >> frontend
    frontend >> users
