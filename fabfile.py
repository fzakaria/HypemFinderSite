from fabric.api import run


def deploy():
	local("./manage test hypemfinder")
	local("git add -p && git commit")
	local("git push")

def host_type():
	run('uname -s')

def git_pull():
	"""Updates the repository"""
	pass
