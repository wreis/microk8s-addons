import sh

from ruamel.yaml import YAML

from utils import microk8s_enable, wait_for_pod_state, microk8s_disable


yaml = YAML(typ="safe")


class TestAddons(object):
    def test_python_demo_nginx(self):
        microk8s_enable("python-hello-k8s")
        wait_for_pod_state("", "default", "running", label="app=python-demo-nginx")
        status = yaml.load(sh.microk8s.status(format="yaml"))
        expected = {"python-hello-k8s": "enabled"}
        microk8s_disable("python-hello-k8s")
