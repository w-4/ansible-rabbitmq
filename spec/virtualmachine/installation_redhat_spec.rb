require 'spec_helper'

if os[:family] == 'redhat'
  describe package('erlang') do
    it { should be_installed }
  end

  describe package('libselinux-python') do
    it { should be_installed }
  end

  describe package('rabbitmq-server') do
    it { should be_installed }
  end
end
