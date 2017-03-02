require 'spec_helper'

describe package('erlang'), :if => os[:family] == 'debian' do
  it { should be_installed }
end

describe package('rabbitmq-server'), :if => os[:family] == 'debian' do
  it { should be_installed }
end
