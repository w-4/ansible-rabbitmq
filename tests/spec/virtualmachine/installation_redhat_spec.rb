require 'spec_helper'

describe package('erlang'), :if => os[:family] == 'redhat' do
  it { should be_installed }
end

describe package('libselinux-python'), :if => os[:family] == 'redhat' do
  it { should be_installed }
end

describe package('rabbitmq-server'), :if => os[:family] == 'redhat' do
  it { should be_installed }
end
