# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  synced_host_dir = "./"
  synced_guest_dir = "/vagrant"

  config.vm.define "master" do |m|
    m.vm.box = "bento/centos-7.3"
    m.vm.box_check_update = false

    m.vm.hostname = "master"
    m.vm.network "private_network", ip: "192.168.33.131", virtualbox__intnet: "intnet"
    m.vm.synced_folder synced_host_dir, synced_guest_dir

    m.vm.provider "virtualbox" do |m_vb|
      m_vb.cpus = 1
      m_vb.memory = "724"
    end

    m.vm.provision "shell" do |sh|
      sh.env   = {
        "http_proxy" => ENV['http_proxy'],
        "https_proxy" => ENV['https_proxy']
      }
      sh.inline = <<-SHELL
        bash /vagrant/install_tools/install_pip.sh
        bash /vagrant/install_tools/install_ansible.sh
      SHELL
    end
  end

  config.vm.define "mongo1" do |s1|
    s1.vm.box = "bento/centos-7.3"
    s1.vm.box_check_update = false

    s1.vm.network "private_network", ip: "192.168.33.132", virtualbox__intnet: "intnet"
    s1.vm.hostname = "mongo1"
    s1.vm.synced_folder synced_host_dir, synced_guest_dir

    s1.vm.provider "virtualbox" do |s1_vb|
      s1_vb.cpus = 1
      s1_vb.memory = "724"
    end
  end

  config.vm.define "mongo2" do |s2|
    s2.vm.box = "bento/centos-7.3"
    s2.vm.box_check_update = false

    s2.vm.network "private_network", ip: "192.168.33.133", virtualbox__intnet: "intnet"
    s2.vm.hostname = "mongo2"

    s2.vm.synced_folder synced_host_dir, synced_guest_dir

    s2.vm.provider "virtualbox" do |s2_vb|
      s2_vb.cpus = 1
      s2_vb.memory = "724"
    end
  end

  config.vm.define "mongo3" do |s3|
    s3.vm.box = "bento/centos-7.3"
    s3.vm.box_check_update = false

    s3.vm.network "private_network", ip: "192.168.33.134", virtualbox__intnet: "intnet"
    s3.vm.hostname = "mongo3"

    s3.vm.synced_folder synced_host_dir, synced_guest_dir

    s3.vm.provider "virtualbox" do |s3_vb|
      s3_vb.cpus = 1
      s3_vb.memory = "724"
    end
  end
end
