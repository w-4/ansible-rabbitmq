require 'spec_helper'

if os[:family] == 'debian'
  describe package('erlang') do
    it { should be_installed }
  end

  describe package('rabbitmq-server') do
    it { should be_installed }
  end
end
