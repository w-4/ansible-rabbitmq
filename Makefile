# ====================================================================================
# Ansible - Dependencies
# ====================================================================================
init:
	pipenv sync

install-dependencies:
	pipenv install --dev $(args)
	pipenv shell

update-roles:
	@pipenv run ansible-galaxy install -r requirements.yml --force $(args)

update-roles-source:
	@pipenv run ansible-galaxy install -g -r requirements.yml --force $(args)

check-roles:
	# look under the roles subdirs for git repos with status changes
	find -L roles*/ -mindepth 1 -maxdepth 2 -type d -name .git -execdir sh -c "git status --porcelain | grep -qv '?? meta/.galaxy_install_info'" \; -exec echo CHANGED: {} \;

# run:
# 	@pipenv run ansible-playbook -i src/envs/production-chicago1 src/configuration/infra-config-linux.yml -l azuredisplacement_financial $(args)
