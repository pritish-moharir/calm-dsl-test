# THIS FILE IS AUTOMATICALLY GENERATED.
# Disclaimer: Please test this file before using in production.
"""
Generated blueprint DSL (.py)
"""

import json  # no_qa
import os  # no_qa

from calm.dsl.builtins import *  # no_qa
from calm.dsl.runbooks import CalmEndpoint as Endpoint

# Secret Variables

BP_CRED_MicrosoftSQLServerPASSWORDCredential_PASSWORD = read_local_file(
    "BP_CRED_MicrosoftSQLServerPASSWORDCredential_PASSWORD"
)

# Credentials
BP_CRED_MicrosoftSQLServerPASSWORDCredential = basic_cred(
    "username",
    BP_CRED_MicrosoftSQLServerPASSWORDCredential_PASSWORD,
    name="MicrosoftSQLServerPASSWORDCredential",
    type="PASSWORD",
)


class MicrosoftSQLServerService(Service):
    """
    MicrosoftSQLServerService module
    Actions:
        All actions starting and ending with `__`(double-underscore) are system actions. Rest are custom actions.
        System actions allowed at service module: __create__, __start__, __stop__, __delete__, __restart__, __soft_delete__
        User can create any custom action also at service level. (Their name dont start and end with double underscore)
    """

    @action
    def __create__():
        """System action for service reate. Action runs when service is created"""

        CalmTask.Exec.escript.py2(
            name="Task_0",
            filename=os.path.join(
                "scripts",
                "Service_MicrosoftSQLServerService_Action___create___Task_Task_0.py",
            ),
        )

        CalmTask.Exec.escript.py2(
            name="Task_1",
            filename=os.path.join(
                "scripts",
                "Service_MicrosoftSQLServerService_Action___create___Task_Task_1.py",
            ),
        )

        CalmTask.Exec.escript.py2(
            name="Task_2",
            filename=os.path.join(
                "scripts",
                "Service_MicrosoftSQLServerService_Action___create___Task_Task_2.py",
            ),
        )

    @action
    def __delete__():
        """System action for service delete. Action runs when service is deleted"""

        CalmTask.Exec.escript.py2(
            name="Task_0",
            filename=os.path.join(
                "scripts",
                "Service_MicrosoftSQLServerService_Action___delete___Task_Task_0.py",
            ),
        )

    @action
    def __start__():
        """System action for service star. Action runs when service is started"""

        CalmTask.Exec.escript.py2(
            name="Task_0",
            filename=os.path.join(
                "scripts",
                "Service_MicrosoftSQLServerService_Action___start___Task_Task_0.py",
            ),
        )

        CalmTask.Exec.escript.py2(
            name="Task_1",
            filename=os.path.join(
                "scripts",
                "Service_MicrosoftSQLServerService_Action___start___Task_Task_1.py",
            ),
        )

    @action
    def __stop__():
        """System action for service stop. Action runs when service is stopped"""

        CalmTask.Exec.escript.py2(
            name="Task_0",
            filename=os.path.join(
                "scripts",
                "Service_MicrosoftSQLServerService_Action___stop___Task_Task_0.py",
            ),
        )

        CalmTask.Exec.escript.py2(
            name="Task_1",
            filename=os.path.join(
                "scripts",
                "Service_MicrosoftSQLServerService_Action___stop___Task_Task_1.py",
            ),
        )

    @action
    def __restart__():
        """System action for service restar. Action runs when service is restarted"""

        CalmTask.Exec.escript.py2(
            name="Task_0",
            filename=os.path.join(
                "scripts",
                "Service_MicrosoftSQLServerService_Action___restart___Task_Task_0.py",
            ),
        )

        CalmTask.Exec.escript.py2(
            name="Task_1",
            filename=os.path.join(
                "scripts",
                "Service_MicrosoftSQLServerService_Action___restart___Task_Task_1.py",
            ),
        )

        CalmTask.Exec.escript.py2(
            name="Task_2",
            filename=os.path.join(
                "scripts",
                "Service_MicrosoftSQLServerService_Action___restart___Task_Task_2.py",
            ),
        )


class MicrosoftSQLServerLinuxAHV_VMSubstrateVmResources(AhvVmResources):

    memory = 1
    vCPUs = 1
    cores_per_vCPU = 1
    disks = [
        AhvVmDisk.Disk.Pci.cloneFromImageService("Centos7HadoopMaster"),
        AhvVmDisk.Disk.Pci.cloneFromImageService("CentOS-7-cloudinit"),
        AhvVmDisk.Disk.Scsi.cloneFromImageService("Centos7HadoopMaster", bootable=True),
        AhvVmDisk.CdRom.Ide.emptyCdRom(),
    ]
    nics = [
        AhvVmNic.NormalNic.ingress(
            "vlan.800", cluster="auto_cluster_prod_f32e476963be"
        ),
        AhvVmNic.NormalNic.ingress(
            "vlan1211", cluster="auto_cluster_prod_f32e476963be"
        ),
        AhvVmNic.NormalNic.ingress(
            "vlan_static", cluster="auto_cluster_prod_f32e476963be"
        ),
    ]


class MicrosoftSQLServerLinuxAHV_VMSubstrate(Substrate):
    """
    Substrate module for MicrosoftSQLServerLinuxAHV_VM. It contains following vm-confugration:
        Disks count: 3
        Nics count: 3
        CdRom count: 1
    provider_spec:
        It defines the provider-vm configuration that will be provisioned.
    readiness_probe:
        It defines set of parameters to get the services status on the vm, i.e. timeout, delay etc.
    Actions:
        All actions starting and ending with `__`(double-underscore) are system actions. No custom actions allowed at substrate level
        System actions allowed at substrate module: __pre_create__, __post_delete__
    """

    os_type = "Linux"
    provider_type = "AHV_VM"
    provider_spec = ahv_vm(
        name="@@{calm_application_name}@@-@@{calm_array_index}@@",
        resources=MicrosoftSQLServerLinuxAHV_VMSubstrateVmResources,
    )

    readiness_probe = readiness_probe(
        connection_type="SSH",
        disabled=False,
        retries="5",
        connection_port=22,
        address="@@{ip_address}@@",
        delay_secs="0",
        credential=ref(BP_CRED_MicrosoftSQLServerPASSWORDCredential),
    )

    @action
    def __pre_create__():
        """Action runs before vm is created"""

        CalmTask.Exec.escript.py2(
            name="Task_0",
            filename=os.path.join(
                "scripts",
                "Substrate_MicrosoftSQLServerLinuxAHV_VMSubstrate_Action___pre_create___Task_Task_0.py",
            ),
        )

        CalmTask.Exec.escript.py2(
            name="Task_1",
            filename=os.path.join(
                "scripts",
                "Substrate_MicrosoftSQLServerLinuxAHV_VMSubstrate_Action___pre_create___Task_Task_1.py",
            ),
        )

        CalmTask.Exec.escript.py2(
            name="Task_2",
            filename=os.path.join(
                "scripts",
                "Substrate_MicrosoftSQLServerLinuxAHV_VMSubstrate_Action___pre_create___Task_Task_2.py",
            ),
        )

    @action
    def __post_delete__():
        """Action runs after vm is deleted"""

        CalmTask.Exec.escript.py2(
            name="Task_0",
            filename=os.path.join(
                "scripts",
                "Substrate_MicrosoftSQLServerLinuxAHV_VMSubstrate_Action___post_delete___Task_Task_0.py",
            ),
        )


class MicrosoftSQLServerPackage(Package):
    """
    Package module for MicrosoftSQLServer
    Actions:
        All actions starting and ending with `__`(double-underscore) are system actions. No custom action are allowed at package level.
        System actions allowed at package module:
            1. __install__ : Action runs to install some libraries once vm is created
            2. __uninstall__ : Action runs to uninstall some libraries before vm is deleted
    Services:
        Define service-reference for the package.

    """

    services = [ref(MicrosoftSQLServerService)]

    @action
    def __install__():

        CalmTask.Exec.escript.py2(
            name="Task_0",
            filename=os.path.join(
                "scripts",
                "Package_MicrosoftSQLServerPackage_Action___install___Task_Task_0.py",
            ),
        )

    @action
    def __uninstall__():

        CalmTask.Exec.escript.py2(
            name="Task_0",
            filename=os.path.join(
                "scripts",
                "Package_MicrosoftSQLServerPackage_Action___uninstall___Task_Task_0.py",
            ),
        )

        CalmTask.Exec.escript.py2(
            name="Task_1",
            filename=os.path.join(
                "scripts",
                "Package_MicrosoftSQLServerPackage_Action___uninstall___Task_Task_1.py",
            ),
        )


class MicrosoftSQLServerDeployment(Deployment):
    """
    Deployment module for MicrosoftSQLServer.
    It contains the  process of installing, configuring, updating, and enabling one application or suite of applications that make a software system available for use.
    It also contains replicas details for scalein and scaleout actions
    Substrate:
        Contains the reference to substrate i.e. vm-configuration and readiness details
    Package:
        Contains the reference to package (internally to service configuration too)
    """

    min_replicas = "2"
    max_replicas = "3"
    default_replicas = "2"

    packages = [ref(MicrosoftSQLServerPackage)]
    substrate = ref(MicrosoftSQLServerLinuxAHV_VMSubstrate)


class MicrosoftSQLServerProfile(Profile):
    """
    Profile module for MicrosoftSQLServer.
    It contains defination to deployments. When a blueprint a launched, one of the profile will be translated to application.
    Actions:
        User can add any custom action here.
        No system actions are allowed at profile level

    """

    deployments = [MicrosoftSQLServerDeployment]


class MicrosoftSQLServerBlueprint(Blueprint):
    """
    MicrosoftSQLServerBlueprint module
    It mainly contains definitions of all the entities i.e. packages, services etc.
    Given blueprint uses:
        - PASSWORD type credential
        - Linux type os for the vm
        - Guest customization enablement status: False
        - Deployment having min-replicas: 2, max:replicas: 3
    """

    services = [MicrosoftSQLServerService]
    packages = [MicrosoftSQLServerPackage]
    substrates = [MicrosoftSQLServerLinuxAHV_VMSubstrate]
    profiles = [MicrosoftSQLServerProfile]
    credentials = [BP_CRED_MicrosoftSQLServerPASSWORDCredential]
