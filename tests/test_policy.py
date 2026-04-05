def test_my_policy_exists():
    from aic_example_policies.my_policy import MyPolicy
    policy = MyPolicy()
    assert policy.name == "MyPolicy"

def test_my_policy_returns_action():
    from aic_example_policies.my_policy import MyPolicy
    policy = MyPolicy()
    action = policy.get_action({})
    assert "action" in action
