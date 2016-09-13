require 'pathname'
DATA_DIR = Pathname 'catalog'
WRANGLE_DIR = Pathname 'wrangle'
CORRAL_DIR = WRANGLE_DIR / 'corral'
SCRIPTS = WRANGLE_DIR / 'scripts'
DIRS = {
    'fetched' => CORRAL_DIR / 'fetched',
    'compiled' => CORRAL_DIR / 'compiled',
    'published' => DATA_DIR,
}


SRC_AGG_URL = 'http://download.cms.gov/Research-Statistics-Data-and-Systems/'\
              + 'Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Downloads/' \
              + 'Medicare_Physician_and_Other_Supplier_NPI_Aggregate_'\
              + 'CY%s.zip'

SRC_PUF_URL = ('http://download.cms.gov/Research-Statistics-Data-and-Systems/' \
                + 'Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Downloads/' \
                + 'Medicare_Provider_Util_Payment_PUF_CY%s.zip?agree=yes&next=Accept')


URL_STEMS = {
  '2012' => '2012_update',
  '2013' => '2013',
  '2014' => '2014',
}

Z_FILES = {
  '2012-puf' => DIRS['fetched'] / '2012-puf.zip',
  '2013-puf' => DIRS['fetched'] / '2013-puf.zip',
  '2014-puf' => DIRS['fetched'] / '2014-puf.zip',
  '2012-agg' => DIRS['fetched'] / '2012-agg.zip',
  '2013-agg' => DIRS['fetched'] / '2013-agg.zip',
  '2014-agg' => DIRS['fetched'] / '2014-agg.zip',
  # 2014 file becomes:
  # Medicare_Physician_and_Other_Supplier_NPI_Aggregate_CY2014.txt
}

XLS_FILES = {
  DIRS['fetched'] / '2012-agg.csv' =>  DIRS['fetched'] / 'Medicare-Physician-and-Other-Supplier-NPI-Aggregate-CY2012.xlsx',
  DIRS['fetched'] / '2013-agg.csv' =>  DIRS['fetched'] / 'Medicare-Physician-and-Other-Supplier-NPI-Aggregate-CY2013.xlsx',
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

task :unpack_zips => Z_FILES.values.map(&:to_s) do
  sh %Q{unzip -o -d #{DIRS['fetched']} \
        '#{DIRS['fetched'] / '*.zip'}'}
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
  namespace :compiled do
    ['2012', '2013', '2014'].each do |year|
      fetchedname = DIRS['fetched'] / "Medicare_Provider_Util_Payment_PUF_CY#{year}.txt"
      compiledname = DIRS['compiled'] / "payments-#{year}.csv"
      desc "Cleaning payments from #{fetchedname}"
      file compiledname => fetchedname do
        sh %Q{
          python #{SCRIPTS / 'clean_payments.py'} \
          #{fetchedname} > #{compiledname}
        }
      end
    end
  end


  namespace :fetched do
    Z_FILES.each_pair do |slug, zname|
      year, ztype = slug.split('-')
      desc "Download #{year} #{ztype} zip file"
      file zname do
        url = (ztype == 'puf') \
              ?  SRC_PUF_URL % URL_STEMS[year] \
              :  SRC_AGG_URL % URL_STEMS[year]

        sh %Q{curl -o #{zname} '#{url}'}
      end
    end
  end

  namespace :xls_to_csv do
    XLS_FILES.each_pair do |csvname, xlsname|
      desc "Convert #{xlsname} to CSV"
      file csvname => xlsname do
        sh %Q{in2csv --sheet 'DATA'   #{xlsname} > #{csvname}}
      end
    end
  end
end

