https://github.com/argoproj/rollouts-demo/blob/master/examples/analysis/analysis-success-rate.yaml
https://argoproj.github.io/argo-rollouts/features/analysis/
https://github.com/jhandguy/canary-deployment/blob/main/sample-app/helm-charts/argo-rollouts/templates/analysistemplate.yaml


kubectl apply -f ingress-nginx.yaml

❯ helm upgrade prometheus prometheus-community/kube-prometheus-stack \
--namespace prometheus  \
--set prometheus.prometheusSpec.podMonitorSelectorNilUsesHelmValues=false \
--set prometheus.prometheusSpec.serviceMonitorSelectorNilUsesHelmValues=false --create-namespace --install
Release "prometheus" does not exist. Installing it now.
NAME: prometheus
LAST DEPLOYED: Fri Nov 25 10:04:10 2022
NAMESPACE: prometheus
STATUS: deployed
REVISION: 1
NOTES:
kube-prometheus-stack has been installed. Check its status by running:
  kubectl --namespace prometheus get pods -l "release=prometheus"

Visit https://github.com/prometheus-operator/kube-prometheus for instructions on how to create & configure Alertmanager and Prometheus instances using the Operator.

