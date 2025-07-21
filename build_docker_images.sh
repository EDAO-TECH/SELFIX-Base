#!/bin/bash
TIERS=("HomeGuard" "ProSecure" "TrustShield" "PartnerX")
for TIER in "${TIERS[@]}"; do
  echo "🔨 Building image for tier: $TIER"
  docker build -f Dockerfile.base -t edaotech/selfix-$TIER --build-arg TIER=$TIER .
done
