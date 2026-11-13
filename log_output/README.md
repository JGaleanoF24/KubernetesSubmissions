# Log output

Generates a random string (UUID) on startup, keeps it in memory, and prints it with a UTC timestamp every 5 seconds.

```
2026-11-12T14:05:01.123Z: 8523ecb1-c716-4cb6-a044-b9e83bb98e43
2026-11-12T14:05:06.128Z: 8523ecb1-c716-4cb6-a044-b9e83bb98e43
```

## Run locally

```sh
python3 app.py
```

## Run with Docker

```sh
docker build -t log-output .
docker run --rm log-output
```

## Run with Kubernetes (k3d)

1. Build the image and import it into the k3d cluster:

   ```sh
   docker build -t log-output:1.0 .
   k3d image import log-output:1.0 -c k3s-default
   ```

2. Apply the Deployment:

   ```sh
   kubectl apply -f manifests/deployment.yaml
   kubectl rollout status deployment/log-output
   ```

3. Check that it's running and view the logs:

   ```sh
   kubectl get pods -l app=log-output
   kubectl logs -f deployment/log-output
   ```

4. Clean up:

   ```sh
   kubectl delete -f manifests/deployment.yaml
   ```

> The manifest uses `imagePullPolicy: IfNotPresent` so Kubernetes uses the imported image instead of pulling from a registry. If the cluster isn't a local k3d cluster, push the image to a registry (e.g. Docker Hub) and update `image:` in `manifests/deployment.yaml`.
