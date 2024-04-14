class InsuranceCompany:
    def __init__(self):
        self.policies = []

    def add_policy(self, policy):
        self.policies.append(policy)
        print("Policy added successfully.")

    def remove_policy(self, policy_number):
        for policy in self.policies:
            if policy["policy_number"] == policy_number:
                self.policies.remove(policy)
                print("Policy removed successfully.")
                return
        print("Policy not found.")

    def list_policies(self):
        if not self.policies:
            print("No policies found.")
        else:
            print("List of policies:")
            for policy in self.policies:
                print(f"Policy Number: {policy['policy_number']}, Holder: {policy['holder']}, Type: {policy['type']}")


# Sample usage
if __name__ == "__main__":
    insurance_co = InsuranceCompany()

    # Adding policies
    insurance_co.add_policy({"policy_number": 1, "holder": "John Doe", "type": "Life"})
    insurance_co.add_policy({"policy_number": 2, "holder": "Jane Smith", "type": "Health"})
    insurance_co.add_policy({"policy_number": 3, "holder": "Bob Johnson", "type": "Car"})

    # Listing policies
    insurance_co.list_policies()

    # Removing a policy
    insurance_co.remove_policy(2)

    # Listing policies again after removal
    insurance_co.list_policies()
