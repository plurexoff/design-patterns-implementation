"""Factory Method - AFTER: With pattern (centralized object creation)."""

from abc import ABC, abstractmethod
from typing import Type, Dict, Any


class VPS(ABC):
    """Abstract base class for VPS providers."""
    
    def __init__(self, name: str, config: str):
        self.name = name
        self.config = config
    
    @abstractmethod
    def deploy(self) -> str:
        """Deploy VPS instance."""
        pass
    
    @abstractmethod
    def get_cost(self) -> float:
        """Get monthly cost."""
        pass


class AWSVPS(VPS):
    """AWS VPS implementation."""
    provider = "AWS"
    
    def deploy(self) -> str:
        return f"Deploying {self.name} on AWS with config {self.config}"
    
    def get_cost(self) -> float:
        return 50.0


class AzureVPS(VPS):
    """Azure VPS implementation."""
    provider = "Azure"
    
    def deploy(self) -> str:
        return f"Deploying {self.name} on Azure with config {self.config}"
    
    def get_cost(self) -> float:
        return 55.0


class GCPVPS(VPS):
    """GCP VPS implementation."""
    provider = "GCP"
    
    def deploy(self) -> str:
        return f"Deploying {self.name} on GCP with config {self.config}"
    
    def get_cost(self) -> float:
        return 48.0


class DigitalOceanVPS(VPS):
    """DigitalOcean VPS implementation (easy to add now!)."""
    provider = "DigitalOcean"
    
    def deploy(self) -> str:
        return f"Deploying {self.name} on DigitalOcean with config {self.config}"
    
    def get_cost(self) -> float:
        return 45.0


class VPSFactory:
    """✅ Factory Method: Encapsulates object creation logic."""
    
    _creators: Dict[str, Type[VPS]] = {
        "aws": AWSVPS,
        "azure": AzureVPS,
        "gcp": GCPVPS,
        "digitalocean": DigitalOceanVPS,
    }
    
    @classmethod
    def create(cls, provider_type: str, name: str, config: str) -> VPS:
        """Create VPS instance based on provider type."""
        if provider_type not in cls._creators:
            raise ValueError(f"Unknown provider: {provider_type}")
        
        vps_class = cls._creators[provider_type]
        return vps_class(name, config)
    
    @classmethod
    def register(cls, provider_type: str, vps_class: Type[VPS]) -> None:
        """Register new provider (allows runtime extension)."""
        cls._creators[provider_type] = vps_class
    
    @classmethod
    def get_providers(cls) -> list:
        """Get list of available providers."""
        return list(cls._creators.keys())


if __name__ == "__main__":
    print("✅ WITH Factory Method Pattern:\n")
    
    # Client code uses factory
    vps1 = VPSFactory.create("aws", "web-server", "t2.medium")
    vps2 = VPSFactory.create("azure", "app-server", "Standard_B2s")
    vps3 = VPSFactory.create("gcp", "db-server", "e2-medium")
    vps4 = VPSFactory.create("digitalocean", "cache-server", "s-1vcpu-1gb")
    
    servers = [vps1, vps2, vps3, vps4]
    
    for vps in servers:
        print(f"Provider: {vps.provider}")
        print(f"  {vps.deploy()}")
        print(f"  Cost: ${vps.get_cost()}/month\n")
    
    total_cost = sum(vps.get_cost() for vps in servers)
    print(f"Total cost: ${total_cost}/month")
    
    print("\n✨ BENEFITS:")
    print("  ✅ Object creation logic is centralized")
    print("  ✅ Adding new provider only requires adding new class + registering")
    print("  ✅ Client doesn't know about concrete VPS classes")
    print("  ✅ Follows Open/Closed Principle")
    print(f"  ✅ Available providers: {VPSFactory.get_providers()}")
    
    # Dynamic registration
    print("\n🔧 Runtime Extension:")
    
    class LinodeVPS(VPS):
        provider = "Linode"
        
        def deploy(self) -> str:
            return f"Deploying {self.name} on Linode with config {self.config}"
        
        def get_cost(self) -> float:
            return 46.0
    
    VPSFactory.register("linode", LinodeVPS)
    vps5 = VPSFactory.create("linode", "gpu-server", "Linode 32GB")
    print(f"New provider registered: {vps5.provider}")
    print(f"Updated providers: {VPSFactory.get_providers()}")
