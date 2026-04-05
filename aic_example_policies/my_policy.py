class MyPolicy:
    """
    Policy ใหม่ของทีม
    """
    def __init__(self):
        self.name = "MyPolicy"
    
    def get_action(self, observation):
        # TODO: ใส่ logic จริงทีหลัง
        return {"action": "move_forward"}
