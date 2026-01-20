"""Factory Method - BEFORE: Without pattern (hardcoded object creation)."""


class AWSVPS:
    """AWS VPS implementation."""
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.provider = "AWS"
    
    def deploy(self):
        return f"Deploying {self.name} on AWS with config {self.config}"
    
    def get_cost(self):
        return 50  # $50/month


class AzureVPS:
    """Azure VPS implementation."""
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.provider = "Azure"
    
    def deploy(self):
        return f"Deploying {self.name} on Azure with config {self.config}"
    
    def get_cost(self):
        return 55  # $55/month


class GCPVPS:
    """GCP VPS implementation."""
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.provider = "GCP"
    
    def deploy(self):
        return f"Deploying {self.name} on GCP with config {self.config}"
    
    def get_cost(self):
        return 48  # $48/month


def create_vps(provider_type, name, config):
    """❌ PROBLEM: Hardcoded logic, client knows about all types."""
    if provider_type == "aws":
        return AWSVPS(name, config)
    elif provider_type == "azure":
        return AzureVPS(name, config)
    elif provider_type == "gcp":
        return GCPVPS(name, config)
    else:
        raise ValueError(f"Unknown provider: {provider_type}")


if __name__ == "__main__":
    print("❌ WITHOUT Factory Method Pattern:\n")
    
    # Client code hardcodes object creation
    vps1 = create_vps("aws", "web-server", "t2.medium")
    vps2 = create_vps("azure", "app-server", "Standard_B2s")
    vps3 = create_vps("gcp", "db-server", "e2-medium")
    
    print(f"VPS 1: {vps1.deploy()}")
    print(f"VPS 2: {vps2.deploy()}")
    print(f"VPS 3: {vps3.deploy()}")
    print(f"\nTotal cost: ${vps1.get_cost() + vps2.get_cost() + vps3.get_cost()}/month")
    
    print("\n⚠️  PROBLEMS:")
    print("  - Hardcoded logic in create_vps()")
    print("  - Adding new provider requires modifying create_vps()")
    print("  - Client knows about all VPS classes")
    print("  - Violates Open/Closed Principle")
