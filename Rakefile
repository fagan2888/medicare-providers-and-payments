require 'pathname'
DATA_DIR = Pathname 'catalog'
WRANGLE_DIR = Pathname 'wrangle'
CORRAL_DIR = WRANGLE_DIR / 'corral'
SCRIPTS = WRANGLE_DIR / 'scripts'
DIRS = {
    'fetched' => CORRAL_DIR / 'fetched',
    'published' => DATA_DIR,
}


BASE_SRC_URL = ('http://download.cms.gov/Research-Statistics-Data-and-Systems/' \
                + 'Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Downloads/' \
                + 'Medicare_Provider_Util_Payment_PUF_CY%s.zip?agree=yes&next=Accept')

URLS = {
  '2012' => BASE_SRC_URL % '2012_update',
  '2013' => BASE_SRC_URL % '2013',
  '2014' => BASE_SRC_URL % '2014',
}


Z_FILES = {
  '2012' => DIRS['fetched'] / '2012.zip',
  '2013' => DIRS['fetched'] / '2013.zip',
  '2014' => DIRS['fetched'] / '2014.zip'
}


desc 'Setup the directories'
task :setup do
    DIRS.each_value do |p|
        unless p.exist?
            p.mkpath()
            puts "Created directory: #{p}"
        end
    end
end


desc "Fetch all the zips"
task :fetch_zips => [:setup] do
  Z_FILES.each_value{ |zname| Rake::Task[zname].execute }
end


desc "Fetch everything"
task :fetch  => [:setup] do
  F_FILES.each_value{|fn| Rake::Task[fn].execute() }
end

desc "Compile everything"
task :compile  => [:setup] do
  C_FILES.each_value{|fn| Rake::Task[fn].execute() }
end

desc "publish everything"
task :publish  => [:setup] do
  P_FILES.each_value{|fn| Rake::Task[fn].execute() }
end




namespace :files do
  namespace :fetched do
    Z_FILES.each_pair do |year, zname|
      desc "Download #{year} zip file"
      file zname do
        url = URLS[year]
        sh %Q{curl -o #{zname} '#{url}'}
      end
    end
  end
end

