import sh

from ruamel.yaml import YAML

from utils import microk8s_enable, wait_for_pod_state, microk8s_disable


yaml = YAML(typ="safe")


class TestAddons(object):
    def test_jupyterlab(self):
        microk8s_enable(
            "jupyterlab --set image=jupyter/base-notebook:x86_64-ubuntu-22.04"
        )
        wait_for_pod_state(
            pod="",
            namespace="default",
            desired_state="running",
            label="app.kubernetes.io/name=jupyterlab",
        )
        status = yaml.load(sh.microk8s.status(format="yaml"))
        expected = {"jupyterlab": "enabled"}
        microk8s_disable("jupyterlab")
