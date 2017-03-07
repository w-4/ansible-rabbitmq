require 'spec_helper'

describe service('rabbitmq-server') do
  it { should be_enabled }
  it { should be_running }
end

describe package('rabbitmq-server') do
  it { should be_installed.with_version('3.3.5') }
end
