#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later

source "$(dirname "${0}")/ci-env.sh"

export DOCKER_BUILDKIT=1 # Enables using secrets in docker-build

exit_code=0
for dockerfile in ${dockerfiles[@]}; do
	for knot_branch in ${knot_branches["$dockerfile"]}; do
		prepare_img_strings

		echo "[CI] Building $image_tag" >&2

		# use as many cached layers as possible (allowed to fail)
		"$docker_cmd" pull "$image_name:6.0" || true
		"$docker_cmd" pull "$image_name:master" || true
		"$docker_cmd" pull "$image_tag" || true

		set +e
		"$docker_cmd" build \
			--build-arg "KNOT_BRANCH=$knot_branch" \
			--tag "$image_tag" \
			--file "ci/images/$dockerfile/Dockerfile" \
			${special_args["$dockerfile"]:-} \
			.
		if [ "$?" -ne "0" ]; then
			exit_code=16
			set -e
			continue
		fi
		set -e

		"$docker_cmd" push "$image_tag"
	done
done

if [ "$exit_code" -ne "0" ]; then
	echo "An error occurred" >&2
fi
exit $exit_code
